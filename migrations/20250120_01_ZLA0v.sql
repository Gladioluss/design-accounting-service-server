CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    verify_token VARCHAR(255),
    updated_at TIMESTAMP,
    created_at TIMESTAMP,
    is_admin BOOLEAN,
    is_verify BOOLEAN,
    is_deleted BOOLEAN
);

CREATE TABLE "refresh_token" (
    id UUID PRIMARY KEY,
    user_id UUID,
    refresh_token VARCHAR(255),
    created_at TIMESTAMP
);

CREATE TABLE "construction" (
    id UUID PRIMARY KEY,
    barcode_number INTEGER,
    properties JSON
);

CREATE TABLE "work_type" (
    id UUID PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE "task" (
    id UUID PRIMARY KEY,
    construction_id UUID,
    user_id UUID,
    work_type_id UUID
);


ALTER TABLE "refresh_token" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);

ALTER TABLE "task" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);
ALTER TABLE "task" ADD FOREIGN KEY (construction_id) REFERENCES "construction" (id);
ALTER TABLE "task" ADD FOREIGN KEY (work_type_id) REFERENCES "work_type" (id);