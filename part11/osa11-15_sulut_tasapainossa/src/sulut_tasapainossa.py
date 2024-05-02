def sulut_tasapainossa(merkkijono: str):
    sulut = ''.join(merkki for merkki in merkkijono if merkki in ['(', ')', '[', ']', '{', '}'])
    if len(sulut) == 0:
        return True
    if not ((sulut[0] == '(' and sulut[-1] == ')') or (sulut[0] == '[' and sulut[-1] == ']') or (sulut[0] == '{' and sulut[-1] == '}')):
        return False

    return sulut_tasapainossa(sulut[1:-1])


if __name__ == '__main__':
    ok = sulut_tasapainossa("([([])])")
    print(ok)

    ok = sulut_tasapainossa("(python versio [3.7]) käytä tätä!")
    print(ok)

    # ei kelpaa sillä virheellinen loppusulku
    ok = sulut_tasapainossa("(()]")
    print(ok)


    # ei kelpaa sillä erityyppiset sulut menevät ristiin
    ok = sulut_tasapainossa("([huono)]")
    print(ok)