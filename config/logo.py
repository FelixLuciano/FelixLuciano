import platform
import socket
import sys


def get_local_address():
    """https://stackoverflow.com/a/28950776/13587869
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.settimeout(0)

    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        address = s.getsockname()[0]
    except Exception:
        address = '127.0.0.1'
    finally:
        s.close()

    return address


uname = platform.uname()


print(f"\33[90m\33[1m            ^εξ                \33[0m\33[1m\33[97m{uname.node}\33[0m")
print(f"\33[90m\33[1m           :πθθι               \33[0m\33[90m{uname.system} {uname.release} ({uname.version})\33[0m")
print( "\33[90m\33[1m          .ββεθθ~              \33[0m")
print( "\33[90m\33[1m          ρβ ιθθε^             \33[0mLocal:", get_local_address())
print( "\33[90m\33[1m         ψπ:  ξθθπ:            \33[0m")
print( "\33[90m\33[1m        ξε^    ζθθπ:           \33[0m")
print( "\33[90m\33[1m       ιθι      ψθθβ.          \33[0m")
print( "\33[90m\33[1m      ~θξ        φθθσ.         \33[0m")
print( "\33[90m\33[1m     :εψ          ρθθρ         \33[0m")
print( "\33[90m\33[1m    :πβ           .πθθφ        \33[0m\33[40m\33[30mLUC\33[41m\33[31mLUC\33[42m\33[32mLUC\33[43m\33[33mLUC\33[44m\33[34mLUC\33[45m\33[35mLUC\33[46m\33[36mLUC\33[47m\33[37mLUC\33[0m")
print( "\33[90m\33[1m  ιζπθπζ~       .ιξπθθθσζ~     \33[0m\33[100m\33[90mLUC\33[101m\33[91mLUC\33[102m\33[92mLUC\33[103m\33[93mLUC\33[104m\33[94mLUC\33[105m\33[95mLUC\33[106m\33[96mLUC\33[107m\33[97mLUC\33[0m")
print("")
