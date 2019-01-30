from octopus.platforms.EOS.disassembler import EosDisassembler

# complete wasm module
file_name = "../eosnameswaps.wasm"


def dissassemble():
    # read file
    with open(file_name, 'rb') as f:
        raw = f.read()

    # just disassembly
    disasm = EosDisassembler()

    # because we provide full module bytecode
    # we need to use disassemble_module()
    # otherwise just disassemble() is enough
    text = disasm.disassemble_module(raw, r_format="text")
    print(text)
    # func 0
    # get_local 0
    # get_local 1
    # i32.const 32
    # call 12
    # i32.eqz
    # end 
    #
    # func 1
    # get_local 0
    # i64.load 3, 0
    # get_local 0
    # i64.load 3, 8
    # call 6
    # end 
    #
    # func 2
    # ...
    # end 
    #
    # ...

if __name__ == "__main__":
    dissassemble()    
