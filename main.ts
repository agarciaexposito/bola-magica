input.onGesture(Gesture.Shake, function () {
    let lista: number[] = []
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.Chessboard)
    basic.pause(100)
    pos = randint(0, lista.length)
    basic.showString("" + (citas[pos]))
})
let pos = 0
let citas: string[] = []
citas = [
"EL MUNDO PERTENECE A QUIÉN SE ATREVE",
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
"PUEDE"
]
