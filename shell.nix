let
  pkgs = import <nixpkgs> {};
  python = pkgs.python312;
  pythonPackages = python.pkgs;
  lib-path = with pkgs; lib.makeLibraryPath [
  ];
in 
pkgs.mkShell {
  packages = with pythonPackages; [
    pygobject3 
    gst-python                # Saw error: "GStreamer element appsink not found. Please install it."
    numpy
    pandas
  ];

  buildInputs = with pkgs; [
    webkitgtk
    # libffi
    # stdenv.cc.cc
  ];

  shellHook = ''
    # For webkitgtk to find glib-networking services
    export GIO_EXTRA_MODULES="${pkgs.glib-networking}/lib/gio/modules:$GIO_EXTRA_MODULES"
    export "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${lib-path}"
    VENV=.venv

    if test ! -d $VENV; then
      ${python.interpreter} -m venv $VENV
    fi
    source ./$VENV/bin/activate
    pip install -r requirements.txt
    zsh
  '';

}