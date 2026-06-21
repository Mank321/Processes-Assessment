from ursina import *

class HealthBar(Entity):
    def __init__(self, max_value, value, position, scale, colour=color.red, bg_colour=color.black, text_size=1, origin=(-.5,.5), roundness=0.1):
        super().__init__()
        self.bg = Entity(parent=camera.ui, model='quad', color=color.black, scale=scale, position=position, origin=origin)
        self.bar = Entity(parent=camera.ui, model='quad', color=color.red, scale=scale, position=position, origin=origin, z=-.005)

        self.max_value = max_value
        self.value = value
        self.position = position
        self.x = position[0]
        self.y=position[1]
        self.scale = scale
        self.color=colour
        self.bg_colour = bg_colour

        self.text = Text(parent=camera.ui, text=f'{self.value}/{self.max_value}', text_size=text_size, position=((self.x+scale[0]/2)-Text.size, self.y-(scale[1]/2)+(Text.size)/2), z=-0.1)

    def update(self):
        if 0 <= self.value <= self.max_value:
            self.bar.scale_x = (self.value/self.max_value)*self.scale[0]
            self.text.text=f'{self.value}/{self.max_value}'
        elif self.value < 0:
            self.value = 0
        else:
            self.value = self.max_value
        if self.value == 0:
            self.bar.enabled = False
        else:
            self.bar.enabled = True
        
        if self.value < 0:
            self.value = 0


if __name__ == '__main__':
    app = Ursina()
    health_bar = HealthBar(10,5,(0.3,0.3),(.2,.1))

    def input(key):
        if key == 'escape':
            application.quit()
        if key == 'p':
            health_bar.value += (-1)
        if key == 'q':
            health_bar.value += 1
    
    app.run()
