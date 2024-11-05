export type UserType = {
    id: number;
    name: string;
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    avatar: string | null;
    bio: string | null;
    permissions: {
        ADMIN: boolean;
        STAFF: boolean;
    };
};

export type AuthenticatedType = {
    authenticated: boolean;
};