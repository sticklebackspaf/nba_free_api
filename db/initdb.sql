CREATE TABLE responses (    key TEXT PRIMARY KEY,    value BLOB,     expires INTEGER);
CREATE INDEX expires_idx ON responses(expires);

CREATE TABLE redirects (    key TEXT PRIMARY KEY,    value BLOB,     expires INTEGER);