{ pkgs }: {
    deps = [
      pkgs.haskellPackages.servant-multipart-client
        pkgs.w3m-batch
        pkgs.w3m
        pkgs.hugo
		pkgs.miniserve
    ];
}