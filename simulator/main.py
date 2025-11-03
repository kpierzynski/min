import math
import sys
import time

import pygame
from simpful import FuzzySystem, LinguisticVariable, TriangleFuzzySet

pygame.init()

FPS = 60
SIM_DURATION = 5 * 60.0

RED = (220, 40, 40)
BLUE = (40, 40, 220)
YELLOW = (255, 255, 80)


class Track:
    def __init__(self, image_path, finish_line=None):
        pygame.display.set_mode((1, 1))

        self.image = pygame.image.load(image_path).convert()
        self.width, self.height = self.image.get_size()
        self.surface = self.image.copy()

        self.mask = pygame.mask.from_threshold(self.surface, (60, 60, 60), (100, 100, 100))

        if finish_line is None:
            finish_line = ((340, 118), (340, 166))
        self.finish_line = finish_line
        pygame.draw.line(self.surface, RED, self.finish_line[0], self.finish_line[1], 2)

    def draw(self, win):
        win.blit(self.surface, (0, 0))

    def is_on_track(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        return self.mask.get_at((int(x), int(y)))

    def is_on_finish_line(self, x, y):
        x1, y1 = self.finish_line[0]
        x2, y2 = self.finish_line[1]
        return min(x1, x2) - 2 <= x <= max(x1, x2) + 2 and min(y1, y2) <= y <= max(y1, y2)


class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0
        self.max_speed = 6
        self.acceleration = 0.2
        self.brake_deceleration = 0.4
        self.free_deceleration = 0.05
        self.turn_speed = 1
        self.width = 30
        self.height = 15
        self.laps = 0
        self.has_crossed_line = False
        self.crashed = False

    def update(self, keys, track):
        if keys[pygame.K_UP]:
            self.speed += self.acceleration
        elif keys[pygame.K_DOWN]:
            self.speed -= self.brake_deceleration
        else:
            if self.speed > 0:
                self.speed -= self.free_deceleration

        self.speed = max(0, min(self.speed, self.max_speed))

        if keys[pygame.K_LEFT]:
            self.angle -= self.turn_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.turn_speed

        self.move(track)

    def apply_fuzzy_control(self, steer, throttle, track):
        self.angle += steer * 0.2

        if throttle > 0:
            self.speed += self.acceleration * throttle
        elif throttle < 0:
            self.speed += throttle * self.brake_deceleration
        else:
            if self.speed > 0:
                self.speed -= self.free_deceleration

        self.speed = max(0, min(self.speed, self.max_speed))
        self.move(track)

    def move(self, track):
        if self.speed > 0:
            rad = math.radians(self.angle)
            new_x = self.x + math.cos(rad) * self.speed
            new_y = self.y + math.sin(rad) * self.speed

            if not track.is_on_track(new_x, new_y):
                self.crashed = True
                return

            self.x, self.y = new_x, new_y
        self.check_lap(track)

    def check_lap(self, track):
        if track.is_on_finish_line(self.x, self.y):
            if not self.has_crossed_line:
                self.laps += 1
                self.has_crossed_line = True
        else:
            self.has_crossed_line = False

    def draw(self, win):
        car_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        car_surf.fill(BLUE)
        rotated = pygame.transform.rotate(car_surf, -self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        win.blit(rotated, rect.topleft)

    def cast_sensor(self, track, offset_deg, max_dist=300):
        base_angle = self.angle + offset_deg
        rad = math.radians(base_angle)
        step = 2
        for dist in range(0, max_dist, step):
            sx = self.x + math.cos(rad) * dist
            sy = self.y + math.sin(rad) * dist
            if not track.is_on_track(sx, sy):
                return dist
        return max_dist

    def read_sensors(self, track):
        L = self.cast_sensor(track, -45)
        F = self.cast_sensor(track, 0)
        R = self.cast_sensor(track, 45)
        return {"L": L, "F": F, "R": R}

    def draw_sensors(self, win, track):
        sensors = [(-45, "left"), (0, "front"), (45, "right")]
        for offset, _ in sensors:
            dist = self.cast_sensor(track, offset)
            rad = math.radians(self.angle + offset)
            hx = self.x + math.cos(rad) * dist
            hy = self.y + math.sin(rad) * dist
            pygame.draw.line(win, YELLOW, (self.x, self.y), (hx, hy), 2)
            pygame.draw.circle(win, RED, (int(hx), int(hy)), 4)

    def get_speed(self):
        return self.speed


class FuzzyController:
    def __init__(self):
        self.FS = FuzzySystem()

        distance_sets = [
            TriangleFuzzySet(0, 0, 0, "Close"),
            ...
        ]

        speed_sets = [
            ...,
        ]

        self.FS.add_linguistic_variable("Left", LinguisticVariable(distance_sets, universe_of_discourse=[0, 300]))
        ...

        steer_sets = [
            ...
        ]

        throttle_sets = [
            ...,
            TriangleFuzzySet(0.0, 0.0, 0.0, "Accelerate")
        ]

        self.FS.add_linguistic_variable(
            "Steer",
            LinguisticVariable(steer_sets, universe_of_discourse=[-50, 50])
        )
        self.FS.add_linguistic_variable(
            "Throttle",
            LinguisticVariable(throttle_sets, universe_of_discourse=[-1.0, 1.0])
        )

        self.FS.add_rules([
            "IF (Left IS Close) AND (Right IS Far) THEN (Steer IS Right)",
            ...
        ])

    def compute(self, L, F, R, V):
        self.FS.set_variable("Left", L)
        self.FS.set_variable("Front", F)
        self.FS.set_variable("Right", R)
        self.FS.set_variable("Speed", V)
        result = self.FS.Mamdani_inference()
        return result["Steer"], result["Throttle"]


def main():
    track_path = "track3.png"
    track = Track(track_path, finish_line=((400, 144), (400, 182)))

    WIN = pygame.display.set_mode((track.width, track.height))
    pygame.display.set_caption(f"Fuzzy Simulation: {track_path}")

    start_x = track.finish_line[0][0] + 25
    start_y = (track.finish_line[0][1] + track.finish_line[1][1]) / 2
    car = Car(start_x, start_y, 0)

    fuzzy = FuzzyController()
    use_fuzzy = True

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    start_time = time.time()

    running = True
    while running:
        clock.tick(FPS)
        elapsed = time.time() - start_time
        remaining = SIM_DURATION - elapsed

        if remaining <= 0:
            print(f"Time is over! Laps: {car.laps}")
            running = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                use_fuzzy = not use_fuzzy
                print(f"Controller: {'FUZZY' if use_fuzzy else 'MANUAL'}")

        keys = pygame.key.get_pressed()

        if use_fuzzy:
            sensors = car.read_sensors(track)
            steer, throttle = fuzzy.compute(sensors["L"], sensors["F"], sensors["R"], car.get_speed())
            car.apply_fuzzy_control(steer, throttle, track)
        else:
            car.update(keys, track)

        if car.crashed:
            print(f"Crashed after {elapsed:.1f}s. Laps: {car.laps}")
            running = False
            break

        track.draw(WIN)
        car.draw(WIN)
        car.draw_sensors(WIN, track)

        WIN.blit(font.render(f"Time: {int(remaining)}s", True, RED), (10, 10))
        WIN.blit(font.render(f"Lap: {car.laps}", True, RED), (10, 35))
        WIN.blit(font.render(f"Speed: {car.get_speed():.2f}", True, RED), (10, 60))
        WIN.blit(font.render(f"Mode: {'FUZZY [A]' if use_fuzzy else 'MANUAL [A]'}", True, RED), (10, 85))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
