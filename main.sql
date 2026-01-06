create table if not exists public.login_user
(
    id        uuid default gen_random_uuid()                                      not null
        constraint login_user_pk
            primary key,
    user_name varchar(50)                                                         not null,
    psd       varchar(255)                                                        not null,
    create_at date default (CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Shanghai'::text) not null
);

comment on column public.login_user.id is '主键';

comment on column public.login_user.user_name is '用户名';

comment on column public.login_user.psd is '加密密码';

comment on column public.login_user.create_at is '注册时间';

alter table public.login_user
    owner to postgres;

create table if not exists public.beta_code
(
    id         uuid default gen_random_uuid() not null
        constraint beta_code_pk
            primary key,
    code       varchar(50)                    not null
        constraint beta_code_pk_2
            unique,
    create_at  date default (CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Shanghai'::text),
    user_by_id uuid
        constraint beta_code_login_user_id_fk
            references public.login_user
);

comment on table public.beta_code is '内测码表';

comment on column public.beta_code.id is '表id';

comment on column public.beta_code.code is '内测码';

comment on column public.beta_code.create_at is '生成时间';

comment on column public.beta_code.user_by_id is '使用者';

alter table public.beta_code
    owner to postgres;

create index if not exists idx_beta_code_unused
    on public.beta_code (user_by_id);

