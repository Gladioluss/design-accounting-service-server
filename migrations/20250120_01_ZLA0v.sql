CREATE TABLE IF NOT EXISTS "user" (
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

CREATE TABLE IF NOT EXISTS "refresh_token" (
    id UUID PRIMARY KEY,
    user_id UUID,
    refresh_token VARCHAR(255),
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "construction" (
    id UUID PRIMARY KEY,
    barcode_number INTEGER,
    updated_at TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "work_type" (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    updated_at TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "task" (
    id UUID PRIMARY KEY,
    is_done BOOLEAN,
    construction_id UUID,
    user_id UUID,
    work_type_id UUID,
    updated_at TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "defect" (
    id UUID PRIMARY KEY,
    barcode_id UUID,
    defect_type VARCHAR(255),
    description TEXT,
    photo VARCHAR(255),
    user_id UUID,
    scan_time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "stage_check" (
    id UUID PRIMARY KEY,
    check_name VARCHAR(255),
    user_id UUID,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "check_measurement" (
    id UUID PRIMARY KEY,
    stage_check_id UUID,
    field_name VARCHAR(255),
    field_value VARCHAR(255),
    created_at TIMESTAMP
);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'refresh_token_user_id_fkey'
          AND table_name = 'refresh_token'
    ) THEN
        ALTER TABLE "refresh_token" 
            ADD CONSTRAINT refresh_token_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user" (id);
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'task_user_id_fkey'
          AND table_name = 'task'
    ) THEN
        ALTER TABLE "task" 
            ADD CONSTRAINT task_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user" (id);
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'task_construction_id_fkey'
          AND table_name = 'task'
    ) THEN
        ALTER TABLE "task" 
            ADD CONSTRAINT task_construction_id_fkey FOREIGN KEY (construction_id) REFERENCES "construction" (id);
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'task_work_type_id_fkey'
          AND table_name = 'task'
    ) THEN
        ALTER TABLE "task" 
            ADD CONSTRAINT task_work_type_id_fkey FOREIGN KEY (work_type_id) REFERENCES "work_type" (id);
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'defect_barcode_id_fkey'
          AND table_name = 'defect'
    ) THEN
        ALTER TABLE "defect" 
            ADD CONSTRAINT defect_barcode_id_fkey FOREIGN KEY (barcode_id) REFERENCES "construction" (id);
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'defect_user_id_fkey'
          AND table_name = 'defect'
    ) THEN
        ALTER TABLE "defect" 
            ADD CONSTRAINT defect_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user" (id);
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'stage_check_user_id_fkey'
          AND table_name = 'stage_check'
    ) THEN
        ALTER TABLE "stage_check" 
            ADD CONSTRAINT stage_check_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user" (id);
    END IF;
END$$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints
        WHERE constraint_name = 'check_measurement_stage_check_id_fkey'
          AND table_name = 'check_measurement'
    ) THEN
        ALTER TABLE "check_measurement" 
            ADD CONSTRAINT check_measurement_stage_check_id_fkey FOREIGN KEY (stage_check_id) REFERENCES "stage_check" (id);
    END IF;
END$$;