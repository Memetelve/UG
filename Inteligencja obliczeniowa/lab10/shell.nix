{ pkgs ? import <nixpkgs> {}, config ? {} }:
let
  pythonPackages = pkgs.python3.withPackages (ps: [
    ps.gym
    ps.gymnasium
    ps.pybox2d
    ps.pygame
    ps.matplotlib
  ]);
in
pkgs.mkShell {
  name = "name";
  buildInputs = [
    (pythonPackages)
  ];
  shellHook = ''
    export PYTHONPATH="${pythonPackages}:${PYTHONPATH:-}"
  '';
}
