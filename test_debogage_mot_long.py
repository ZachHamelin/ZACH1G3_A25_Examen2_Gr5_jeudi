from debogage_mot_long import mot_plus_long, pourcentage_mots_max  # Remplacer par le nom de ton fichier

# ============================
# Tests pour mot_plus_long
# ============================
# TODO: Tests unitaires pour la fonction mot_plus_long (maximum 5 différents)
def test_mot_plus_long():
    mots = ["poney", "girafe", "hippopotame"]
    resultat = mot_plus_long(mots)

    assert resultat == "hippopotame"


def test_mot_plus_long_meme_nb_lettre():
    mots = ["chaton", "girafe"]
    resultat = mot_plus_long(mots)

    assert resultat == "chaton", "girafe"

def test_mot_plus_long_vide():
    mots = []
    resultat = mot_plus_long(mots)

    assert resultat is None

def test_mot_plus_long_chiffre():
    mots = ["chaton", "poney", 42]
    resultat = mot_plus_long(mots)

    assert resultat == "chaton"

def test_mot_plus_long_pas_liste():
    mots = "chaton"
    resultat = mot_plus_long(mots)

    assert resultat == None

# ============================
# Tests pour pourcentage_mots_max
# ============================
def test_pourcentage_mots_max_normal():
    mots = ["poney", "girafe", "hippopotame", "chaton"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 75.0

def test_pourcentage_mots_max_tous_superieur():
    """
    Lorsque tous les mots présents dépassent la taille,
    le pourcentage retourné est 100%.
    """
    mots = ["éléphant", "hippopotame", "girafe"]
    resultat = pourcentage_mots_max(mots, 4)

    assert resultat == 100.0

def test_pourcentage_mots_max_elements_invalides():
    mots = ["pamplemousse", 42, "cacahuète", None]
    resultat = pourcentage_mots_max(mots, 8)

    assert resultat == 100.0

def test_pourcentage_mots_max_liste_vide():
    mots = []
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat is None

def test_pourcentage_mots_max_tous_inferieur():
    """
    Lorsque tous les mots présents sont
    plus petits que la taille, le pourcentage
    retourné est 0.0%.
    """
    mots = ["chat", "chien", "rat"]
    resultat = pourcentage_mots_max(mots, 5)

    assert resultat == 0.0

def test_pourcentage_mots_max_tous_inferieur():
    mots = 7
    resultat = pourcentage_mots_max(mots, 3)

    assert resultat == None