package org.kirish.candyservicetesting.utils;

import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.stereotype.Component;

@Component
public class Generator {

    public String randomAlphaNumeric(int min, int max) {
        return RandomStringUtils.randomAlphanumeric(min, max);
    }

}
