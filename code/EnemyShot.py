from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        # Inicializa o tiro do inimigo com nome e posição
        super().__init__(name, position)

    def move(self, ):
        # Move o tiro do inimigo para a esquerda de acordo com sua velocidade
        self.rect.centerx -= ENTITY_SPEED[self.name]
