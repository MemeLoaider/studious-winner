package org.kirish.candyservicetesting.tests;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.kirish.candyservicetesting.BaseTest;
import org.kirish.candyservicetesting.dto.Candy;

public class PositiveTest extends BaseTest {

    @Test
    @DisplayName("Get single candy test")
    public void getSingleCandyTest() {
        Candy candy = CANDY_SERVICE.getSingleCandyByID("3");
        LOGGER.info("Retrieved candy: {}", candy);
    }

}
