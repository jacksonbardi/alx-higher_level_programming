#!/user/bin/python3
# Author - bamidele Adefolaju

def remove_chae_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1])
