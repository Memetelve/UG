"use client";

import React, { useState } from "react";
import { useSession } from "next-auth/react";

export default function AddMeeting() {
    const [desc, setDesc] = useState("");
    const [date, setDate] = useState("");
    const [start, setStart] = useState("");
    const [end, setEnd] = useState("");
    const { data: session, status } = useSession();

    const handleSubmit = async (e) => {
        e.preventDefault();

        const body = JSON.stringify({ desc, date, start, end });
        const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/meetings/add`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + session.access_token,
            },
            body,
        });
        if (res.ok) {
            setDesc("");
            setDate("");
            setStart("");
            setEnd("");
            alert("Meeting added");
        } else {
            console.log(res);
            alert("An error occurred");
        }
    };

    if (status == "loading") {
        return (
            <main>
                <h1 className="text-4xl text-center">Add Meeting</h1>
                <div className="text-center text-2xl">Loading...</div>
            </main>
        );
    }

    return (
        <main>
            <h1 className="text-4xl text-center">Add Meeting</h1>
            <form className="mt-6 ml-auto mr-auto text-neutral-600" onSubmit={handleSubmit}>
                <label className="block text-lg" htmlFor="desc">
                    Description
                </label>
                <input
                    className="border border-gray-500 p-1 w-full"
                    type="text"
                    id="desc"
                    name="desc"
                    value={desc}
                    onChange={(e) => setDesc(e.target.value)}
                    required
                />
                <label className="block text-lg" htmlFor="date">
                    Date
                </label>
                <input
                    className="border border-gray-500 p-1 w-full"
                    type="date"
                    id="date"
                    name="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                />
                <label className="block text-lg" htmlFor="start">
                    Start hour
                </label>
                <input
                    className="border border-gray-500 p-1 w-full"
                    type="time"
                    id="start"
                    name="start"
                    value={start}
                    onChange={(e) => setStart(e.target.value)}
                    required
                />
                <label className="block text-lg" htmlFor="end">
                    End hour
                </label>
                <input
                    className="border border-gray-500 p-1 w-full"
                    type="time"
                    id="end"
                    name="end"
                    value={end}
                    onChange={(e) => setEnd(e.target.value)}
                    required
                />
                <button
                    className="bg-blue-900 text-white p-2 mt-4 w-full"
                    type="submit"
                >
                    Add
                </button>
            </form>
        </main>
    );
}
