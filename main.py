from js import document, window
keys = {}


def draw_player():
    ctx.fillStyle = "cyan"
    ctx.fillRect(player["x"], player["y"], player["size"], player["size"])


def draw_coin():
    ctx.fillStyle = "gold"
    ctx.beginPath()
    ctx.arc(
        coin["x"],
        coin["y"],
        coin["size"],
        0,
        2 * 3.14159
    )
    ctx.fill()


def update():
    global score

    if keys.get("ArrowUp"):
        player["y"] -= player["speed"]

    if keys.get("ArrowDown"):
        player["y"] += player["speed"]

    if keys.get("ArrowLeft"):
        player["x"] -= player["speed"]

    if keys.get("ArrowRight"):
        player["x"] += player["speed"]

    # Collision detection
    if (
        player["x"] < coin["x"] + coin["size"] and
        player["x"] + player["size"] > coin["x"] - coin["size"] and
        player["y"] < coin["y"] + coin["size"] and
        player["y"] + player["size"] > coin["y"] - coin["size"]
    ):
        score += 1
        score_text.innerHTML = f"Score: {score}"

        coin["x"] = random.randint(50, 550)
        coin["y"] = random.randint(50, 350)


def draw():
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    draw_player()
    draw_coin()


def game_loop(*args):
    update()
    draw()

    window.requestAnimationFrame(game_loop_proxy)


def key_down(event):
    keys[event.key] = True


def key_up(event):
    keys[event.key] = False


keydown_proxy = create_proxy(key_down)
keyup_proxy = create_proxy(key_up)
game_loop_proxy = create_proxy(game_loop)


document.addEventListener("keydown", keydown_proxy)
document.addEventListener("keyup", keyup_proxy)

window.requestAnimationFrame(game_loop_proxy)
