package com.example.springcalculator.controller;

import com.example.springcalculator.component.Cal;
import com.example.springcalculator.dto.Req;
import com.example.springcalculator.dto.Res;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
public class Api {

    private final Cal cal;

    @GetMapping("/sum")
    public int sum(@RequestParam int x, @RequestParam int y){
        return cal.sum(x, y);
    }

    @PostMapping("/minus")
    public Res minus(@RequestBody Req req){

        int result = cal.minus(req.getX(), req.getY());
        Res res = new Res();
        res.setResult(result);
        res.setResponse(new Res.Body());

        return res;
    }
}
