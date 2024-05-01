/*
This DDL is intended to be initial structure of the core job table.
 */
begin;

create extension if not exists "uuid-ossp";

-- I don't suspect the following enums to grow
create type if not exists compensation_type as enum ('salary', 'hourly');

-- could be used as a multiplier for amount to determine things like yearly or hourly rates
create type if not exists employment_type as enum ('permanent', 'contract');

create table
    if not exists compensation (
        guid uuid primary key,
        compensation_type compensation_type,
        amount money, -- may require investigating the system default lc_money
    );

create table
    if not exists address_entities (guid uuid primary key,);

create table
    if not exists job (
        guid uuid primary key,
        name text not null constraint name_len_check check (char_length(name) <= 255),
        overview text,
        qualifications text,
        responsibilities text,
        date_posted date,
        date_applied date,
        creation_date timestamp not null default current_timestamp,
        employment_type employment_type,
        contract_length interval year compensation_guid uuid references compensation (guid),
    );

commit;