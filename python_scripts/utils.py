
def esc(code):
    """Utility for wrapping ANSI escape codes for pretty printing."""
    return f'\033[{code}m'

def ansify(text, code):
    return esc(code) + text + esc(0)
