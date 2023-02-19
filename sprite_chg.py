import json

with open('sprite.json', 'r') as f:
    json_sprite = json.load(f)

class Sprite:
    def __init__(self, obj, texture):
        self.obj = obj
        self.texture_size = self.obj['texture_size']
        self.elements = self.obj['elements']
        self.from_ = self.elements['from']
        self.to = self.elements['to']
        self.faces = self.elements['faces']

    def change(self, pixel_changes, texture):
        pass

sprite = Sprite(json_sprite, 'sprite.png')

sprite.change()