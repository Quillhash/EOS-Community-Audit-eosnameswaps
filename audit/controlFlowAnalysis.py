from octopus.platforms.EOS.cfg import EosCFG

# complete wasm module
file_name = "../eosnameswaps.wasm"


def controlFlowAnalysis():
    # read file
    with open(file_name, 'rb') as f:
        raw = f.read()

    # create the cfg
    cfg = EosCFG(raw)

    # visualize
    cfg.visualize_call_flow()


if __name__ == "__main__":
    controlFlowAnalysis()
