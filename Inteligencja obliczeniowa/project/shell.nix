{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.libgccjit
  ];

  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.libgccjit}/lib"
  '';
}

