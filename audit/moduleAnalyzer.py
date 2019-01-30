from octopus.platforms.EOS.analyzer import EosAnalyzer

# complete wasm module
file_name = "../eosnameswaps.wasm"


def runTest():
   with open(file_name, 'rb') as f:
       module_bytecode = f.read()

   # return list of functions instructions (list)
   # attributes analysis=True by default
   analyzer = EosAnalyzer(module_bytecode)

   # show analyzer attributes
   print(analyzer.func_prototypes)
   #[('action_data_size', '', 'i32', 'import'), ('eosio_assert', 'i32 i32', '', 'import'), ('eosio_exit', 'i32', '', 'import'), ('memcpy', 'i32 i32 i32', 'i32', 'import'), ('prints', 'i32', '', 'import'), ('read_action_data', 'i32 i32', 'i32', 'import'), ('require_auth2', 'i64 i64', '', 'import'), ('_ZeqRK11checksum256S1_', 'i32 i32', 'i32', 'export'), ('_ZN5eosio12require_authERKNS_16permission_levelE', 'i32', '', 'export'), ('apply', 'i64 i64 i64', '', 'export'), ('$func10', 'i32 i64', '', 'local'), ('$func11', 'i32 i32', 'i32', 'local'), ('memcmp', 'i32 i32 i32', 'i32', 'export'), ('malloc', 'i32', 'i32', 'export'), ('$func14', 'i32 i32', 'i32', 'local'), ('$func15', 'i32', 'i32', 'local'), ('free', 'i32', '', 'export'), ('$func17', '', '', 'local')]
   print()
   print(analyzer.exports)
   # [{'field_str': 'memory', 'kind': 2, 'index': 0}, {'field_str': '_ZeqRK11checksum256S1_', 'kind': 0, 'index': 7}, {'field_str': '_ZN5eosio12require_authERKNS_16permission_levelE', 'kind': 0, 'index': 8}, {'field_str': 'apply', 'kind': 0, 'index': 9}, {'field_str': 'memcmp', 'kind': 0, 'index': 12}, {'field_str': 'malloc', 'kind': 0, 'index': 13}, {'field_str': 'free', 'kind': 0, 'index': 16}]
   print()
   print(analyzer.imports_func)
   # [('env', 'action_data_size', 3), ('env', 'eosio_assert', 5), ('env', 'eosio_exit', 2), ('env', 'memcpy', 6), ('env', 'prints', 2), ('env', 'read_action_data', 4), ('env', 'require_auth2', 1)]

if __name__ == "__main__":
    runTest()   