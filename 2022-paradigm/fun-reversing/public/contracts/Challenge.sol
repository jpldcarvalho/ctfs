pragma solidity 0.8.16;

contract Challenge {
    function solved() public returns (bool) {
        //v0, v1 = _challenge.staticcall(0x799320bb).gas(msg.gas);
        //require(v0); // checks call status, propagates error data on error
        //require(MEM[64] + RETURNDATASIZE() - MEM[64] >= 32);
        //require(v1 == v1);
        //return v1;
        var var0 = 0x00;
        var var1 = storage[0] & (0x01 << 0xa0) - 0x01 & (0x01 << 0xa0) - 0x01;
        var var2 = 0x799320bb;
        var temp0 = memory[0x40:0x60];
        memory[temp0:temp0 + 0x20] = (var2 & 0xffffffff) << 0xe0;
        var var3 = temp0 + 0x04;
        var temp1 = memory[0x40:0x60];
        var temp2;
        temp2, memory[temp1:temp1 + 0x20] = address(var1).staticcall.gas(msg.gas)(memory[temp1:temp1 + var3 - temp1]);
        var var4 = !temp2;
    
        if (!var4) {
            var temp3 = memory[0x40:0x60];
            var temp4 = returndata.length;
            memory[0x40:0x60] = temp3 + (temp4 + 0x1f & ~0x1f);
            var1 = 0x00fb;
            var2 = temp3 + temp4;
            var3 = temp3;
            return func_0100(var2, var3);
        } else {
            var temp5 = returndata.length;
            memory[0x00:0x00 + temp5] = returndata[0x00:0x00 + temp5];
            revert(memory[0x00:0x00 + returndata.length]);
        }
    }

    function func_0100(var arg0, var arg1) returns (var r0) {
        var var0 = 0x00;
    
        if (arg0 - arg1 i< 0x20) { revert(memory[0x00:0x00]); }
    
        var temp0 = memory[arg1:arg1 + 0x20];
        var var1 = temp0;
    
        if (var1 == !!var1) { return var1; }
        else { revert(memory[0x00:0x00]); }
    }
}
