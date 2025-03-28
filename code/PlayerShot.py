from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        # Chama o construtor da classe pai (Entity)
        super().__init__(name, position)

    def move(self, ):
        # Move o tiro do jogador para a direita com base na velocidade definida em ENTITY_SPEED
        self.rect.centerx += ENTITY_SPEED[self.name]
