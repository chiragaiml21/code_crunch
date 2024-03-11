import express from 'express'
import { PythonShell } from "python-shell";
import cors from "cors";

const app = express()
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors({ origin: "http://localhost:3001" }));

app.get('/', (req,res)=>{
    res.send('Hello World!')
})

app.post('/api/data',(req,res) => {
    console.log("Hello")

    try {
        PythonShell.run("assistant.py", null)
          .then(messages => console.log(messages))
      } catch (error) {
        console.error("Error creating index:", error);
        res
          .status(500)
          .json({ error: "An error occurred while creating the index" });
      }
})

app.listen(3000, ()=>{
    console.log(`Server is running on port : http://localhost:3000`)
})