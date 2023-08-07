# shape
 A (very simple) animatable IDE
# Commands
    - rect x1 y1 x2 y2 fill outline: Creates a rectangle / square
    - line x1 y1 x2 y2 fill: Creates a line
    - oval x1 y1 x2 y2 fill outline: Creates an oval / circle
    - arc x1 y1 x2 y2 fill outline: Creates an arc
    - text x y fill text: Creates text
    - clear: Clears the canvas
    - wait seconds: Waits seconds
# Examples
    - Code:
        text 100 100 white abc
        wait 0.5
        clear
        text 200 200 white def
        wait 0.5
        clear
    - Explanation:
        write "abc" at x=100, y=100
        wait 0.5 seconds
        clear canvas
        write "def" at x=200, y=200
        wait 0.5 seconds
        clear