package org.kirish.candyservicetesting.dto;

import com.google.gson.Gson;

public interface DataTransferObject {

    Gson GSON = new Gson();

    default String asJson() {
        return GSON.toJson(this);
    }

    static <T extends DataTransferObject> T fromJson(String stringAsJson, Class<T> tClass) {
        return GSON.fromJson(stringAsJson, tClass);
    }

}
