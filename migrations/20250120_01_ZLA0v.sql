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
    updated_at TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE "work_type" (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    updated_at TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE "task" (
    id UUID PRIMARY KEY,
    is_done BOOLEAN,
    construction_id UUID,
    user_id UUID,
    work_type_id UUID,
    updated_at TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE "defect" (
    id UUID PRIMARY KEY,
    barcode_id UUID,
    defect_type VARCHAR(255),
    description TEXT,
    photo VARCHAR(255),
    user_id UUID,
    scan_time TIMESTAMP
);

CREATE TABLE "stage_check" (
    id UUID PRIMARY KEY,
    check_name VARCHAR(255),
    user_id UUID,
    created_at TIMESTAMP
);

CREATE TABLE "check_measurement" (
    id UUID PRIMARY KEY,
    stage_check_id UUID,
    field_name VARCHAR(255),
    field_value VARCHAR(255),
    created_at TIMESTAMP
);

ALTER TABLE "refresh_token" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);
ALTER TABLE "task" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);
ALTER TABLE "task" ADD FOREIGN KEY (construction_id) REFERENCES "construction" (id);
ALTER TABLE "task" ADD FOREIGN KEY (work_type_id) REFERENCES "work_type" (id);
ALTER TABLE "defect" ADD FOREIGN KEY (barcode_id) REFERENCES "construction" (id);
ALTER TABLE "defect" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);
ALTER TABLE "stage_check" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);
ALTER TABLE "check_measurement" ADD FOREIGN KEY (stage_check_id) REFERENCES "stage_check" (id);
