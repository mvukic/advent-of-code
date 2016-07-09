package com.mvukic.github.adventofcode.day23;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Day23 {
    public int ParsingIndex,RegA,RegB,CommandCounter;
    public List<Command> Commands;

    public static void main(String[] args) {
        Day23 day23 = new Day23();
        day23.ParseIt();
        day23.WorkIt();
    }
    public Day23(){
        this.ParsingIndex=0;
        this.Commands = new ArrayList<>();
        /*
         part1 -> RegA = 0
         part2 -> RegA = 1
         */
        this.RegA = 0;
        this.RegB = 0;
        this.CommandCounter=0;
    }
    public void WorkIt(){
        while (this.CommandCounter < this.Commands.size()){
            Command command = this.Commands
                    .stream()
                    .filter(c -> c.Index == this.CommandCounter)
                    .findFirst()
                    .get();
            System.out.println("Executing command: "+command);
            if (command.Type.equals("jmp_uncond")){
                this.CommandCounter += command.Offset;
                System.out.println("Jumping to "+this.CommandCounter);
            }
            else if(command.Type.equals("jmp_cond")){
                if(command.Cmd.equals("jie")){
                    if(command.Reg.equals("a")){
                        if( RegA % 2 == 0) {
                            this.CommandCounter += command.Offset;
                            System.out.println("\t"+command.Reg +" is even => jumping to command "+this.CommandCounter);
                        }else{
                            this.CommandCounter++;
                            System.out.println("\tCondition not true => next command is "+this.CommandCounter);
                        }
                    }else if(command.Reg.equals("b")){
                        if( RegB % 2 == 0) {
                            this.CommandCounter += command.Offset;
                            System.out.println("\t"+command.Reg +" is even => jumping to command "+this.CommandCounter);
                        }else{
                            this.CommandCounter++;
                            System.out.println("\tCondition not true => next command is "+this.CommandCounter);
                        }
                    }
                }else if(command.Cmd.equals("jio")){
                    if(command.Reg.equals("a")){
                        if( RegA == 1) {
                            this.CommandCounter += command.Offset;
                            System.out.println("\t"+command.Reg +" is 1 => jumping to command "+this.CommandCounter);
                        }else{
                            this.CommandCounter++;
                            System.out.println("\tCondition not true => next command is "+this.CommandCounter);
                        }
                    }else if(command.Reg.equals("b")){
                        if( RegB == 1) {
                            this.CommandCounter += command.Offset;
                            System.out.println("\t"+command.Reg +" is 1 => jumping to command "+this.CommandCounter);
                        }else{
                            this.CommandCounter++;
                            System.out.println("\tCondition not true => next command is "+this.CommandCounter);
                        }
                    }
                }

            }else if(command.Type.equals("reg_op")){
                if(command.Cmd.equals("hlf")){
                    if(command.Reg.equals("a")){
                        this.RegA /= 2;
                    }else if(command.Reg.equals("b")){
                        this.RegB /= 2;
                    }
                }
                if(command.Cmd.equals("tpl")){
                    if(command.Reg.equals("a")){
                        this.RegA *= 3;
                    }else if(command.Reg.equals("b")){
                        this.RegB *= 3;
                    }
                }
                if(command.Cmd.equals("inc")){
                    if(command.Reg.equals("a")){
                        this.RegA++;
                    }else if(command.Reg.equals("b")){
                        this.RegB++;
                    }
                }
                System.out.println("Next command is "+this.Commands.get(this.CommandCounter));
               this.CommandCounter++;
            }
            System.out.format("\tSTATUS:\n\tRegA : %d\n\tRegB : %d\n\tCommandCounter : %d\n",this.RegA,this.RegB,this.CommandCounter);
        }
        System.out.println("Finished executing program.");
    }
    public void ParseIt(){
        try {
            this.Commands = Files.lines(Paths.get("input.txt"))
                    .map(this::ParseLine)
                    .collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        };
    }

    public Command ParseLine(String line){
        String[] temp = line.split(" ");
        Command command = null;
        if (temp.length == 3) {
            int offset=0;
            if (temp[2].contains("+")){
                offset = Integer.parseInt(temp[2].substring(1,temp[2].length()));
            }else{
                offset = -1*Integer.parseInt(temp[2].substring(1,temp[2].length()));
            }
            command = new Command(this.ParsingIndex,"jmp_cond",temp[0],temp[1].substring(0,temp[1].length()-1),offset);
        }else if(temp.length == 2){
            if (temp[0].equals("jmp")){
                int offset=0;
                if (temp[1].contains("+")){
                    offset = Integer.parseInt(temp[1].substring(1,temp[1].length()));
                }else{
                    offset = -1*Integer.parseInt(temp[1].substring(1,temp[1].length()));
                }
                command = new Command(this.ParsingIndex,"jmp_uncond",temp[0],null,offset);
            }else{
                command = new Command(this.ParsingIndex,"reg_op",temp[0],temp[1],null);
            }
        }
        this.ParsingIndex++;
        return command;
    }
}
