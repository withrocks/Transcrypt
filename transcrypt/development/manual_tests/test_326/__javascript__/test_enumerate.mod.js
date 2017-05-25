	(function () {
		var enumerate_string = function () {
			for (var [ix, c] of enumerate ('abc')) {
				print (ix, c);
			}
		};
		__pragma__ ('<all>')
			__all__.enumerate_string = enumerate_string;
		__pragma__ ('</all>')
	}) ();
