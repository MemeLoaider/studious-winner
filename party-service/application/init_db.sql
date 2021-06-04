CREATE DATABASE IF NOT EXISTS party;

USE party;

CREATE TABLE IF NOT EXISTS party_stuff (
	party_id INT AUTO_INCREMENT PRIMARY KEY,
	host VARCHAR(50),
	place VARCHAR(100),
	number_of_ppl INT
);

INSERT INTO party_stuff (host, place, number_of_ppl)
SELECT "Crystal", "Park Ave.", 100 FROM DUAL
WHERE NOT EXISTS (
	SELECT *
	FROM party_stuff
	WHERE host = "Crystal" AND place = "Park Ave." AND number_of_ppl = 100
	LIMIT 1
);

INSERT INTO party_stuff (host, place, number_of_ppl)
SELECT "Boi$Noi$", "Underground Dumpster 79", 70 FROM DUAL
WHERE NOT EXISTS (
	SELECT *
	FROM party_stuff
	WHERE host = "Boi$Noi$" AND place = "Underground Dumpster 79" AND number_of_ppl = 70
	LIMIT 1
);

INSERT INTO party_stuff (host, place, number_of_ppl)
SELECT "V3RoniKO", "Plaza Shlaza WC", 250 FROM DUAL
WHERE NOT EXISTS (
	SELECT *
	FROM party_stuff
	WHERE host = "V3RoniKO" AND place = "Plaza Shlaza WC" AND number_of_ppl = 250
	LIMIT 1
);
