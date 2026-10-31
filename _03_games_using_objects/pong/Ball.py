class Ball:

    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.x_speed = 4
        self.y_speed = 4
        self.size = 20
        self.hit_paddle = False

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        # Bounce off left and right walls
        if self.x < self.size/2 or self.x > width - self.size/2:
            self.x_speed *= -1

        # Bounce off top wall
        if self.y < self.size/2:
            self.y_speed *= -1

    def draw(self):
        fill(255)
        ellipse(self.x, self.y, self.size, self.size)

    def collision(self, paddle):
        # Check if ball hits paddle
        if (self.y + self.size/2 >= paddle.y - paddle.height/2
            and self.y_speed > 0
            and self.x + self.size/2 >= paddle.x - paddle.width/2
            and self.x - self.size/2 <= paddle.x + paddle.width/2):

            self.y_speed *= -1
            self.y = paddle.y - paddle.height/2 - self.size/2

            return True

        return False
