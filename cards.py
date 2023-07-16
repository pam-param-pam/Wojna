import random
import logging
import time

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♣', '♦', '♥']

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Create the deck
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)
# Split the deck between players
half1 = deck[:26]
half2 = deck[26:]
round_num = 1


# Game loop
while half1 and half2:
    card1 = half1.pop(0)
    card2 = half2.pop(0)

    logger.debug("Gracz 1 kładzie kartę: %s", card1)
    logger.debug("Gracz 2 kładzie kartę: %s", card2)

    if ranks.index(card1[0]) > ranks.index(card2[0]):
        logger.debug("Gracz 1 wygrywa rundę!")
        half1.extend([card1, card2])
    elif ranks.index(card1[0]) < ranks.index(card2[0]):
        logger.debug("Gracz 2 wygrywa rundę!")
        half2.extend([card2, card1])
    else:
        logger.info("Wojna!")
        war_cards = [card1, card2]
        while True:
            if len(half1) < 2:
                logger.info("Nie można kontynuować wojny. Gra zakończona.")
                logger.info(f"Liczba rund: {round_num}")
                logger.info("Gracz 2 wygrywa grę!")
                exit()
            if len(half2) < 2:
                logger.info("Nie można kontynuować wojny. Gra zakończona.")
                logger.info(f"Liczba rund: {round_num}")
                logger.info("Gracz 1 wygrywa grę!")
                exit()

            card1_hidden = half1.pop(0)
            card2_hidden = half2.pop(0)

            logger.debug("Gracz 1 kładzie zakrytą kartę.")
            logger.debug("Gracz 2 kładzie zakrytą kartę.")

            card1 = half1.pop(0)
            card2 = half2.pop(0)

            war_cards.extend([card1_hidden, card2_hidden, card1, card2])  # Use extend instead of append

            logger.debug("Gracz 1 kładzie kartę: %s", card1)
            logger.debug("Gracz 2 kładzie kartę: %s", card2)

            if ranks.index(card1[0]) > ranks.index(card2[0]):
                logger.debug("Gracz 1 wygrywa wojnę!")
                half1.extend(war_cards)
                break
            elif ranks.index(card1[0]) < ranks.index(card2[0]):
                logger.debug("Gracz 2 wygrywa wojnę!")
                half2.extend(war_cards)
                break
            else:
                logger.debug("Wojna trwa dalej!")

    logger.info(f"Runda: {round_num}")
    logger.info(f"Player1 has : {len(half1)}")
    logger.info(f"Player2 has : {len(half2)}")


    round_num += 1
# Game result
logger.info("\n--- KONIEC GRY ---")
logger.info(f"Zagrano rund: {round_num}")

if len(half1) == 0:
    logger.info("Gracz 2 wygrywa grę!")
else:
    logger.info("Gracz 1 wygrywa grę!")
