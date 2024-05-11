with import <nixpkgs> {};

let
  localPython = writeScriptBin "local-python" ''
    ./env/bin/python "$@"
  '';

  python = runCommand "python" {
    nativeBuildInputs = [ makeWrapper ];
    buildInputs = [ pkgs.stdenv.cc.cc localPython ];
  } ''
    makeWrapper ${localPython}/bin/local-python $out/bin/py \
      --prefix LD_LIBRARY_PATH : ${pkgs.stdenv.cc.cc}/lib \
      --prefix LD_LIBRARY_PATH : /run/opengl-driver/lib/
  '';
in python
