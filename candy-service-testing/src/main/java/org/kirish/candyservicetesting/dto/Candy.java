package org.kirish.candyservicetesting.dto;

import lombok.Data;

@Data
public class Candy implements DataTransferObject {

    private String id;
    private String name;

}
