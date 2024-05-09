# let
#   pkgs = import <nixpkgs> {};
# in pkgs.mkShell {
#   packages = [
#     (pkgs.python3.withPackages (python-pkgs: [
#       # python-pkgs.pandas
#       # python-pkgs.numpy
#       # python-pkgs.matplotlib
#       python-pkgs.tensorflowWithCuda
#       # python-pkgs.keras
#       # python-pkgs.scikit-learn
#     ]))
#   ];
# }
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
