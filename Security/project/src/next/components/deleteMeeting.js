"use client";

import React, { useState } from "react";
import { useSession } from "next-auth/react";

export default function DeleteMeeting({ id }) {
    const { data: session, status } = useSession();

    const handleClick = async (e) => {
        e.preventDefault();

        const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/meetings/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                Authorization: "Bearer " + session.access_token,
            },
        });
        if (res.ok) {
            alert("Meeting deleted");
        } else {
            console.log(res);
            alert("An error occurred");
        }
    };

    if (status == "loading") {
        return (
            <div className="text-center text-2xl">Loading...</div>
        );
    }

    return (
        <button className="bg-red-500 text-white p-1 rounded" onClick={handleClick}>
            Delete
        </button>
    );
}
