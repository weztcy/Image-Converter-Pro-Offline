from ai.background_remover import BackgroundRemover



def test_background_remover_available():

    remover = BackgroundRemover()


    assert remover.is_available() is True