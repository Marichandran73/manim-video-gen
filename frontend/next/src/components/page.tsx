// ./app/page.tsx
import ClientComponent from "@/components/ClientComponent";
import * as dotenv from "dotenv";
import Eye  from "./ui/eye"; 

dotenv.config();

export default async function Page() {


  // return <ClientComponent accessToken={accessToken} />;
  return <>
      <ClientComponent />
    <Eye /> 
    </>
}
