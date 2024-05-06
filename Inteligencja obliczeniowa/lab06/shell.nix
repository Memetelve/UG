{ pkgs ? import <nixpkgs> {}, config ? {} }:
let
  pythonPackages = pkgs.python3.withPackages (ps: [
    ps.tensorflow
    ps.keras
    ps.tensorflow-estimator
    ps.keras-preprocessing
    ps.keras-applications
    ps.scikit-learn
    ps.pandas
    ps.numpy
  ]);
in
pkgs.mkShell {
  name = "tf";
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      (pkgs.callPackage ./python-packages.nix)
    ]))
  ];
  # buildInputs = [
  #   (pythonPackages)
  # ];
  shellHook = ''
    export PYTHONPATH="${pythonPackages}:${PYTHONPATH:-}"
  '';
}
