export interface InstructorData {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
    expertise: number[]; // Change this type based on your data structure
  }
  interface LoginResponse {
    ok: boolean;
    token: string;
    msg: string;
    id: number;
    name: string;
  }
  