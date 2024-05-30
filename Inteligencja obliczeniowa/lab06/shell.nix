
{ pkgs ? import <nixpkgs> {}, config ? {} }:
let
  pythonPackages = pkgs.python3.withPackages (ps: [
    ps.tensorflow
    ps.keras
    ps.tensorflow-estimator
    ps.keras-preprocessing
    ps.keras-applications
    ps.scikit-learn
    ps.matplotlib
    ps.pydot
    ps.seaborn
    ps.opencv4
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
