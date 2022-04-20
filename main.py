def on_gesture_shake():
    global pos
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.CHESSBOARD)
    basic.pause(100)
    pos = randint(0, 10-1)
    basic.show_string("" + (citas[len(citas)]))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

citas: List[str] = []
pos = 0
citas = ["EL MUNDO PERTENECE A QUIÉN SE ATREVE",
    "JUEGA, RÍE Y DISFRUTA",
    "ASÍ ES LA VIDA, DISFRÚTALA",
    "FELICIDAD",
    "A DISFRUTAR",
    "SILENCIO",
    "PAZ",
    "NO PIDAS PERMISO PARA CAMBIAR",
    "CAMBIA DE CAMINOS",
    "VIVE CADA DÍA",
    "ÁMATE",
    "DI QUE SÍ",
    "DI QUE NO",
    "PUEDE"]

def on_forever():
    pass
basic.forever(on_forever)
