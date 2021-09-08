package com.example.springcalculator.component;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
//ICal을 생성자로 주입하는 것
public class Cal {

    private final ICal iCal;

    public int sum(int x, int y){
        this.iCal.init();
        return this.iCal.sum(x, y);
    }

    public int minus(int x, int y){
        this.iCal.init();
        return this.iCal.minus(x, y);
    }
}

