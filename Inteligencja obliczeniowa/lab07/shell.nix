{ pkgs ? import <nixpkgs> {}, config ? {} }:
let
  pythonPackages = pkgs.python3.withPackages (ps: [
    ps.tensorflow
    ps.keras
    ps.scikit-learn
    ps.matplotlib
    ps.pydot
    ps.seaborn
    ps.optree
    ps.rich
    ps.ml-dtypes
    ps.nltk
  ]);
in
pkgs.mkShell {
  name = "tf";
  buildInputs = [
    (pythonPackages)
  ];
  shellHook = ''
    export PYTHONPATH="${pythonPackages}:${PYTHONPATH:-}"
  '';
}
