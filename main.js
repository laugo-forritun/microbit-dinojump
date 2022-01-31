function fall () {
    if (dinosaur > 4) {
    	dinosaur = 4
        y_speed = 0
    }
    else {
        dinosaur += y_speed
        y_speed += y_acc
    
    }
}

function draw() {
    basic.clearScreen()
    led.plot(0,dinosaur)
    basic.pause(30)
}
input.onButtonPressed(Button.A, function() {
    y_speed -= JUMP_FORCE
})


let dinosaur = 4
let JUMP_FORCE = 0.8
let y_speed = 0
let y_acc = 0.1
basic.forever(function () {
    fall()
    draw()
	
})

