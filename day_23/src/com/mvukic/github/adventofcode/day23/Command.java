package com.mvukic.github.adventofcode.day23;

/**
 * Created by matija on 09.07.16..
 */
public class Command {
    public int Index;
    public String Type;
    public String Cmd;
    public String Reg;
    public Integer Offset;
    public Command(int Index,String Type,String Cmd,String Reg ,Integer Offset){
        this.Index=Index;
        this.Cmd=Cmd;
        this.Offset=Offset;
        this.Reg=Reg;
        this.Type=Type;
    }

    @Override
    public String toString() {
        if (this.Type.equals("jmp_uncond")){
            return String.format("%d : %s %d",this.Index,this.Cmd,this.Offset);
        }
        if(this.Type.equals("jmp_cond")){
            return String.format("%d : %s %s, %d",this.Index,this.Cmd,this.Reg,this.Offset);
        }
        if(this.Type.equals("reg_op")){
            return String.format("%d : %s %s",this.Index,this.Cmd,this.Reg);
        }
        return "";
    }
}
